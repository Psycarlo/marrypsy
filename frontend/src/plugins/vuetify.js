import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#ffffff",
        secondary: "#1b1b1b",
        accent: "#008dd5",
        error: "#ba274a",
        info: "#0892a5",
        success: "#68b684",
        warning: "#f9c846",
        background: "#1b1b1b",
        navigation: "#404040"
      }
    }
  }
});
