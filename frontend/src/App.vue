<template>
  <v-app :style="{ background: $vuetify.theme.themes[theme].background }">
    <v-main>
      <transition name="fade" mode="out-in">
        <router-view></router-view>
      </transition>
    </v-main>
  </v-app>
</template>

<script>
export default {
  computed: {
    theme() {
      return this.$vuetify.theme.dark ? "dark" : "light";
    },
    isNewUser() {
      return this.$store.state.isNewUser;
    }
  },
  created: function() {
    this.$nextTick(function() {
      if (this.isNewUser) {
        this.$router.push("/eighteen");
      }
    });
  }
};
</script>

<style lang="scss">
$body-font-family: "Montserrat", serif;

.fade-enter,
.fade-leave-to {
  opacity: 0;
  transform: translateX(2em);
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.33s ease;
}
</style>
