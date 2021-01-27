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
    <Tinder
      ref="tinder"
      key-name="id"
      :queue.sync="queue"
      :max="3"
      :offset-y="10"
      allow-down
      @submit="onSubmit"
    >
      <template slot-scope="scope">
        <div
          class="pic"
          :style="{
            'background-image': `url(https://cn.bing.com//th?id=OHR.${scope.data.id}_UHD.jpg&pid=hp&w=720&h=1280&rs=1&c=4&r=0)`
          }"
        />
      </template>
      <img class="like-pointer" slot="like" src="../assets/marry.png" />
      <img class="nope-pointer" slot="nope" src="../assets/nope.png" />
      <img class="super-pointer" slot="super" src="../assets/psy.png" />
    </Tinder>
  </div>
</template>

<script>
import Tinder from "@/components/vue-tinder/Tinder.vue";
import source from "@/bing";

export default {
  components: { Tinder },
  data: () => ({
    isLoading: false,
    queue: [],
    offset: 0,
    history: []
  }),
  created() {
    this.mock();
  },
  methods: {
    logout() {
      this.isLoading = true;
      this.$store.dispatch("logout");
      this.isLoading = false;
    },
    mock(count = 5, append = true) {
      const list = [];
      for (let i = 0; i < count; i++) {
        list.push({ id: source[this.offset] });
        this.offset++;
      }
      if (append) {
        this.queue = this.queue.concat(list);
      } else {
        this.queue.unshift(...list);
      }
    },
    onSubmit({ item }) {
      if (this.queue.length < 3) {
        this.mock();
      }
      this.history.push(item);
    },
    async decide(choice) {
      if (choice === "rewind") {
        if (this.history.length) {
          this.$refs.tinder.rewind(
            this.history.splice(-Math.ceil(Math.random() * 3))
          );
        }
      } else if (choice === "help") {
        console.log("Help");
      } else {
        this.$refs.tinder.decide(choice);
      }
    }
  }
};
</script>

<style scoped>
.vue-tinder {
  width: 355px;
  height: 520px;
  min-width: 300px;
  max-width: 355px;
}
</style>
