import type { Config } from "tailwindcss";

const generateStartShadow = (count: number) => {
  let shadowStars = "";
  for (let i = 0; i < count; i++) {
    if (i != 0) {
      shadowStars += ", ";
    }
    const x = Math.random() * 3000 - 0;
    const y = Math.random() * 3000 - 0;

    shadowStars += `${x}px ${y}px white`;
  }
  return shadowStars;
};

const generateStartShadow2 = (count: number) => {
  let shadowStars = "";
  for (let i = 0; i < count; i++) {
    if (i != 0) {
      shadowStars += ", ";
    }
    const x = Math.random() * 3000 - 0;
    const y = Math.random() * 3000 - 0;

    shadowStars += `${x}px ${y}px white`;
  }
  return shadowStars;
};

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        inter: ["var(--font-inter)"],
        poppins: ["var(--font-poppins)"],
        lato: ["var(--font-lato)"],
        playfair_display: ["var(--font-playfair_display)"],
        orbitron: ["var(--font-orbitron)"],
      },
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      screens: {
        mdmax: { max: "767px" },
        // => @media (max-width: 767px) { ... }
      },
      colors: {
        "soft-color": "#182237",
      },
      boxShadow: {
        "custom-combined": generateStartShadow(500),
        "custom-combined-2": generateStartShadow(500),
        "custom-combined-litle": generateStartShadow2(1000),
      },
      keyframes: {
        starsup: {
          "0%": { transform: "translate(0)" },
          "100%": { transform: "translateY(-2000px)" },
        },
      },
      animation: {
        starsup: "starsup 50s linear infinite",
        starsup2: "starsup 30s linear infinite",
      },
    },
  },
  plugins: [require("@xpd/tailwind-3dtransforms")],
};
export default config;
