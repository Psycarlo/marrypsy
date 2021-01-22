<template>
  <div>
    <h1 class="primary--text">[Main: You are authenticated]</h1>
    <v-btn
      dark
      color="success"
      @click="logout"
      :loading="isLoading"
      class="mt-4"
      >{{ $t("labels.logout") }}</v-btn
    >
  </div>
</template>

<script>
export default {
  data: () => ({
    isLoading: false
  }),
  methods: {
    logout() {
      this.isLoading = true;
      this.$store.dispatch("logout");
      this.isLoading = false;
    }
  }
};
</script>
