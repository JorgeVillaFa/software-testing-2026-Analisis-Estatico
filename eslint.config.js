import js from "@eslint/js";

export default [
  js.configs.recommended,
  {
    files: ["**/*.js"],
    ignores: ["node_modules/**"],
    rules: {
      // opcional: reglas extra aquí
    },
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module"
    }
  }
];
