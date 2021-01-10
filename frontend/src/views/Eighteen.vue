<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <h1 class="primary--text text-center">{{ $t("questions.eighteen") }}</h1>
      <v-col cols="12" class="mt-8 text-center">
        <!-- TODO: Below 300px the buttons have no margin top/bottom and are not align center -->
        <v-btn
          class="mr-4 primary--text"
          color="primary"
          outlined
          min-width="120"
          >{{ $t("answers.no") }}</v-btn
        >
        <v-btn class="ml-4 secondary--text" color="primary" min-width="120">{{
          $t("answers.yes")
        }}</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script></script>
