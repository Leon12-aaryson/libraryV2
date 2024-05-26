/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{html,js}"],
  theme: {
    extend: {
      'custom-blue': '#176D81',
      'custom-blue-dark': '#0f4854',
      'custom-google-light': '#D6E4F0',
    },
  },
  plugins: [],
}

