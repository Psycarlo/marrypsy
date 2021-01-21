<template>
  <!-- TODO: Add parallax & bg image? -->
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <h1 class="primary--text text-center">{{ $t("titles.login") }}</h1>
      <v-col cols="12" class="mt-8" align="center">
        <v-form ref="form" v-model="valid" lazy-validation>
          <div style="max-width:420px;">
            <v-text-field
              color="warning"
              dark
              v-model="email"
              :rules="emailRules"
              v-bind:label="$t('labels.email')"
              class="shrink"
              outlined
              required
            ></v-text-field>
            <v-text-field
              color="warning"
              dark
              v-model="password"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="passwordRules"
              :type="showPassword ? 'text' : 'password'"
              v-bind:label="$t('labels.password')"
              outlined
              @click:append="showPassword = !showPassword"
              required
            ></v-text-field>
            <v-btn
              dark
              :disabled="!valid"
              x-large
              block
              color="success"
              @click="submit"
              :loading="isLoading"
              class="mt-4"
              >{{ $t("labels.login") }}</v-btn
            >
          </div>
        </v-form>
      </v-col>
      <p class="primary--text caption mt-8">
        {{ $t("questions.not-registered") }}
        <router-link
          to="/register"
          style="text-decoration:none; font-weight: bold"
          >{{ $t("titles.register") }}</router-link
        >
      </p>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    valid: true,
    email: "",
    password: "",
    showPassword: false,
    isLoading: false
  }),
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        this.isLoading = true;
        this.$store.dispatch("login", {
          email: this.email,
          password: this.password
        });
        this.isLoading = false;
      }
    }
  },
  computed: {
    emailRules() {
      return [
        v => !!v || this.$t("errors.no-email"),
        v => /.+@.+/.test(v) || this.$t("errors.invalid-email")
      ];
    },
    passwordRules() {
      return [v => !!v || this.$t("errors.no-password")];
    }
  }
};
</script>

<style lang="css">
.v-btn--disabled {
  background-color: #313131 !important;
}
</style>
