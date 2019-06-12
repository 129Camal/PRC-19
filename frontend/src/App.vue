<template>
  <v-app dark>
    <v-toolbar flat>
      <v-toolbar-side-icon @click="sideNav =! sideNav"></v-toolbar-side-icon>
      <v-toolbar-title>Cycling World</v-toolbar-title>
      <!-- <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn flat>
          <v-icon left>arrow_forward_ios</v-icon>Login
        </v-btn>
        <v-btn flat>
          <v-icon left>arrow_forward_ios</v-icon>Register
        </v-btn>
      </v-toolbar-items> -->
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
export default {
  name: "App",
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
