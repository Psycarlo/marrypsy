import Vue from "vue";
import Vuex from "vuex";
import VuexPersist from "vuex-persist";
import * as fb from "../firebase";
import router from "../router/index";

const vuexLocal = new VuexPersist({
  storage: window.localStorage
});

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userProfile: {}
  },
  mutations: {
    setUserProfile(state, val) {
      state.userProfile = { ...state.userProfile, ...val };
    },
    setUserInterest(state, val) {
      state.userProfile.interest = val;
    }
  },
  actions: {
    async login({ dispatch }, form) {
      const { user } = await fb.auth.signInWithEmailAndPassword(
        form.email,
        form.password
      );

      dispatch("fetchUserProfile", user);
    },

    async register({ dispatch }, form) {
      const { user } = await fb.auth.createUserWithEmailAndPassword(
        form.email,
        form.password
      );

      await fb.usersCollection.doc(user.uid).set({
        interest: null
      });

      dispatch("getUserInterest", user);
    },

    async logout() {
      // TODO: logout > redirect to home > remove vuex persist
    },

    async fetchUserProfile({ commit }, user) {
      const userProfile = await fb.usersCollection.doc(user.uid).get();

      commit("setUserProfile", userProfile.data());

      router.push("/main");
    },

    async getUserInterest({ commit }, user) {
      const userProfile = await fb.usersCollection.doc(user.uid).get();

      commit("setUserProfile", userProfile.data());

      router.push("/interest");
    },

    async setUserInterest({ commit }, form) {
      const user = fb.auth.currentUser;
      await fb.usersCollection.doc(user.uid).set({
        interest: form.interest
      });

      commit("setUserInterest", form.interest);

      router.push("/main");
    }
  },
  modules: {},
  plugins: [vuexLocal.plugin]
});
