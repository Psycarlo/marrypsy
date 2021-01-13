<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <h1 class="primary--text text-center">{{ $t("questions.interest") }}</h1>
      <v-col cols="12" class="mt-8 text-center">
        <!-- TODO: Below 300px the buttons have no margin top/bottom and are not align center -->
        <v-btn
          class="mr-4 secondary--text"
          color="primary"
          @click="submit('female')"
          min-width="120"
          >{{ $t("answers.females") }}</v-btn
        >
        <v-btn
          class="ml-4 secondary--text"
          color="primary"
          @click="submit('male')"
          min-width="120"
          >{{ $t("answers.males") }}</v-btn
        >
      </v-col>
      <v-col cols="12" class="mt-2 text-center">
        <v-btn
          class="mr-4 primary--text"
          color="primary"
          outlined
          @click="submit('both')"
          min-width="120"
          >{{ $t("answers.both") }}</v-btn
        >
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  methods: {
    submit(interest) {
      this.$store.dispatch("setUserInterest", {
        interest
      });
    }
  }
};
</script>
