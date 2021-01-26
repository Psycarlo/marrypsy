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
    isLoading: false,
    queue: [],
    offset: 0
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

<style scoped>
.vue-tinder {
  width: 335px;
  height: 447px;
}
</style>
