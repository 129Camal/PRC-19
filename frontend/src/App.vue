<template>
  <v-app>
    <v-toolbar>
      <v-toolbar-side-icon @click="sideNav =! sideNav"></v-toolbar-side-icon>
      <v-toolbar-title><v-btn flat to="/" >Cycling World</v-btn></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <Logout/>
        <v-btn v-if="!this.getToken" flat to="/login">Login</v-btn>
      </v-toolbar-items>
    </v-toolbar>
    <v-navigation-drawer app temporary v-model="sideNav">
      <v-list>
        <v-list-tile v-for="item in items" :key="item.title" @click="changeRoute(item)">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <main>
      <router-view></router-view>
    </main>
  </v-app>
</template>

<script>
import Logout from "./components/users/Logout";
import { mapGetters } from "vuex";

export default {
  name: "App",
  computed: mapGetters(["getToken"]),
  components:{
    Logout
  },
  data() {
    return {
      sideNav: false,
      items: [
        { title: "Competitions", icon: "navigate_next" },
        { title: "Athletes", icon: "navigate_next" },
        { title: "Teams", icon: "navigate_next" }
      ]
    };
  },
  methods: {
    changeRoute: function(item) {
      let route = item.title.toLowerCase()
      this.$router.push("/" + route)
    }
  },
};
</script>

<style>
body {
  background-image: url("https://www.boofeaction.de/blog/wp-content/uploads/2016/05/TheGiro.jpg");
}
</style>
