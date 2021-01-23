<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <h1 class="primary--text text-center">{{ $t("questions.eighteen") }}</h1>
      <v-col cols="12" class="mt-6 text-center">
        <v-btn
          class="mr-4 primary--text btn-eighteen-left"
          color="primary"
          outlined
          min-width="120"
          @click="goToNo"
          >{{ $t("answers.no") }}</v-btn
        >
        <v-btn
          class="ml-4 secondary--text btn-eighteen-right"
          color="primary"
          min-width="120"
          @click="goToYes"
          >{{ $t("answers.yes") }}</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  methods: {
    goToNo() {
      window.location.href = "https://bitcoin.org/bitcoin.pdf";
    },
    goToYes() {
      this.$store.commit("setIsNotNewUser");
      this.$router.push("/");
    }
  }
};
</script>

<style lang="css">
@media only screen and (max-width: 313px) {
  .btn-eighteen-left {
    margin: 0 !important;
    margin-bottom: 10px !important;
    margin-left: 12px !important;
  }
  .btn-eighteen-right {
    margin: 0 !important;
    margin-top: 10px !important;
    margin-right: 18px !important;
  }
}
</style>
