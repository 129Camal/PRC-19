<template>
  <v-btn v-if="this.getToken" flat class="btn btn-info btn-fill btn-wd" v-on:click="doLogout()">LogOut</v-btn>
</template>

<script>
import { mapMutations, mapGetters } from "vuex";


export default {
  name: "Logout",
  computed: mapGetters(["getToken"]),
  methods: {
    ...mapMutations(["removeToken"]),
    doLogout() {
      this.removeToken();
      this.$router.push("/login");
    }
  }
};
</script>
