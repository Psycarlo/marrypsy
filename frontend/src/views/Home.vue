<template>
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
        <v-btn class="mr-2primary--text" color="primary" text min-width="120">{{
          $t("titles.signin")
        }}</v-btn>
        <v-btn class="ml-2 primary--text" color="warning" min-width="120">{{
          $t("titles.signup")
        }}</v-btn>
      </v-col>
      <v-col cols="1"></v-col>
    </v-row>
  </v-toolbar>
</template>

<script></script>
