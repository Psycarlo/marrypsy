<template>
  <!-- TODO: Add parallax & bg image? -->
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <h1 class="primary--text text-center">{{ $t("titles.register") }}</h1>
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
              @click="resetAlert"
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
              @click="resetAlert"
              @click:append="showPassword = !showPassword"
              required
            ></v-text-field>
            <v-alert
              :value="alert"
              type="error"
              color="error"
              class="primary--text my-2"
              transition="fade-transition"
            >
              {{ errorMsg }}
            </v-alert>
            <v-btn
              dark
              :disabled="!valid"
              x-large
              block
              color="success"
              @click="submit"
              :loading="isLoading"
              class="mt-4"
              >{{ $t("labels.create-account") }}</v-btn
            >
          </div>
        </v-form>
      </v-col>
      <p class="primary--text caption mt-8">
        {{ $t("questions.already-registered") }}
        <router-link
          to="/login"
          style="text-decoration:none; font-weight: bold"
          >{{ $t("titles.login") }}</router-link
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
    errorMsg: "",
    alert: false,
    showPassword: false,
    isLoading: false
  }),
  methods: {
    resetAlert() {
      this.alert = false;
    },
    async submit() {
      if (this.$refs.form.validate()) {
        this.isLoading = true;
        try {
          await this.$store.dispatch("register", {
            email: this.email.toLowerCase(),
            password: this.password
          });
        } catch (error) {
          this.errorMsg = this.$i18n.t("errors.fb-other-error");
          switch (error.code) {
            case "auth/email-already-exists":
              this.errorMsg = this.$i18n.t("errors.fb-email-already-exists");
              break;
            case "auth/email-already-in-use":
              this.errorMsg = this.$i18n.t("errors.fb-email-already-exists");
              break;
          }
          this.alert = true;
        }
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
      return [
        v => !!v || this.$t("errors.no-password"),
        v => (v && v.length >= 6) || this.$t("errors.invalid-password")
      ];
    }
  }
};
</script>

<style lang="css">
.v-btn--disabled {
  background-color: #313131 !important;
}
</style>
