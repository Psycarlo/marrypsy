<template>
  <div>
    <v-toolbar color="navigation">
      <!-- TODO: Refactor : This shit looks ugly af -->
      <v-row>
        <v-col cols="1"></v-col>
        <v-col cols="8">
          <v-app-bar-nav-icon>
            <v-img
              alt="Vue logo"
              src="../assets/logo.png"
              max-height="80"
              max-width="80"
              contain
            />
          </v-app-bar-nav-icon>
        </v-col>
        <v-col cols="2" class="mt-1">
          <v-btn
            class="mr-2 primary--text"
            color="primary"
            text
            min-width="120"
            @click="navigateLogin"
            >{{ $t("titles.signin") }}</v-btn
          >
          <v-btn
            class="ml-2 primary--text"
            color="warning"
            min-width="120"
            @click="navigateRegister"
            >{{ $t("titles.signup") }}</v-btn
          >
        </v-col>
        <v-col cols="1"></v-col>
      </v-row>
    </v-toolbar>
    <v-row>
      <v-col class="col col-4"
        ><h1 class="primary--text">
          Swipe to <br />
          discover your
        </h1>
        <p class="primary--text">ideal partner</p>
        <v-btn class="ml-2 primary--text" color="warning" min-width="120">{{
          $t("titles.joinnow")
        }}</v-btn>
        <v-btn
          class="mr-2 primary--text text-capitalize"
          color="primary"
          text
          min-width="120"
          >{{ $t("titles.learnmore") }}</v-btn
        ></v-col
      >
      <v-col class="col col-4">
        <v-img
          lazy-src="https://picsum.photos/id/11/10/6"
          max-height="715"
          max-width="474"
          src="@/assets/babe.png"
        ></v-img>
      </v-col>
      <v-col class="col col-4">
        <v-img
          lazy-src="https://picsum.photos/id/11/10/6"
          max-height="715"
          max-width="474"
          src="@/assets/mane.png"
        ></v-img>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  methods: {
    navigateLogin() {
      this.$router.push("/login");
    },
    navigateRegister() {
      this.$router.push("/register");
    }
  }
};
</script>
