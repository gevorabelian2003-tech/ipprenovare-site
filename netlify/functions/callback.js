// Reçoit le retour de GitHub, échange le code contre un jeton d'accès,
// puis renvoie le jeton à l'interface /admin (Decap CMS) via postMessage.
const https = require("https");

function echangeToken(code) {
  const clientId = process.env.OAUTH_GITHUB_CLIENT_ID;
  const clientSecret = process.env.OAUTH_GITHUB_CLIENT_SECRET;
  const data = JSON.stringify({ client_id: clientId, client_secret: clientSecret, code });
  return new Promise((resolve, reject) => {
    const req = https.request(
      {
        hostname: "github.com",
        path: "/login/oauth/access_token",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "Content-Length": Buffer.byteLength(data),
          "User-Agent": "ipprenovare-cms",
        },
      },
      (res) => {
        let body = "";
        res.on("data", (c) => (body += c));
        res.on("end", () => {
          try {
            resolve(JSON.parse(body));
          } catch (e) {
            reject(e);
          }
        });
      }
    );
    req.on("error", reject);
    req.write(data);
    req.end();
  });
}

exports.handler = async (event) => {
  const code = (event.queryStringParameters || {}).code;
  if (!code) return { statusCode: 400, body: "Code d'autorisation manquant." };

  let status = "error";
  let content = { error: "Échec de l'authentification." };
  try {
    const result = await echangeToken(code);
    if (result.access_token) {
      status = "success";
      content = { token: result.access_token, provider: "github" };
    }
  } catch (e) {
    content = { error: String(e) };
  }

  const message = `authorization:github:${status}:${JSON.stringify(content)}`;
  const body = `<!DOCTYPE html><html><head><meta charset="utf-8"></head><body>
<p style="font-family:sans-serif;text-align:center;margin-top:3rem;">Connexion en cours…</p>
<script>
  (function () {
    function receiveMessage(e) {
      window.opener.postMessage(${JSON.stringify(message)}, e.origin);
      window.removeEventListener("message", receiveMessage, false);
    }
    window.addEventListener("message", receiveMessage, false);
    window.opener.postMessage("authorizing:github", "*");
  })();
</script></body></html>`;

  return { statusCode: 200, headers: { "Content-Type": "text/html" }, body };
};
