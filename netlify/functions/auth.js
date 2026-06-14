// Démarre la connexion GitHub pour l'interface /admin (Decap CMS).
// Redirige l'utilisateur vers la page d'autorisation GitHub.
const crypto = require("crypto");

exports.handler = async (event) => {
  const clientId = process.env.OAUTH_GITHUB_CLIENT_ID;
  if (!clientId) {
    return { statusCode: 500, body: "OAUTH_GITHUB_CLIENT_ID manquant côté serveur." };
  }
  const host = event.headers.host;
  const redirectUri = `https://${host}/.netlify/functions/callback`;
  const state = crypto.randomBytes(12).toString("hex");
  const url =
    "https://github.com/login/oauth/authorize" +
    `?client_id=${encodeURIComponent(clientId)}` +
    `&redirect_uri=${encodeURIComponent(redirectUri)}` +
    "&scope=repo" +
    `&state=${state}`;
  return { statusCode: 302, headers: { Location: url }, body: "" };
};
