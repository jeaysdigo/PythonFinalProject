/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./static/pat/*.{html,js}",
    "./node_modules/tw-elements/dist/js/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        'ubuntu': ['Ubuntu', 'sans-serif'],
      },
    },
  },
  plugins: [
    require("daisyui"),
    require("tw-elements/dist/plugin.cjs")
  ],
  darkMode: "class"
}

