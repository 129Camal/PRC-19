<template>
  <v-container grid-list-xs>
    <v-layout row>
      <v-flex x12 md12>
        <v-toolbar color="grey lighten-2">
          <v-toolbar-title>Login</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <br>
        <br>
        <form>
          <v-text-field v-model="email" label="Email" required></v-text-field>

          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'visibility' : 'visibility_off'"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            @click:append="show1 = !show1"
            required
          ></v-text-field>
          <v-alert :value="alertError" color="amber darken-1" icon="priority_high">
            <b>{{this.msgerror}}</b>
          </v-alert>

          <v-btn @click="submit">Login</v-btn>
          <router-link to="/register">
            <v-btn>Don't have an account?</v-btn>
          </router-link>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import Vue from "vue";
import VeeValidate from "vee-validate";
import { mapMutations } from "vuex";

Vue.use(VeeValidate);

export default {
  name: "login",

  data: () => ({
    show1: false,
    alertError: false,
    msgerror: "",
    email: "",
    password: ""
  }),

  methods: {
    ...mapMutations(["setToken"]),
    submit() {
      axios
        .post("http://localhost:2019/users/login", {
          email: this.email,
          password: this.password
        })
        .then(response => {
          console.log(response.data.status)
          switch (response.data.status) {
            case "OK LOGGED":
              this.alertError = false;
              this.setToken(response.data.acessToken);
              this.$router.push("/competitions");
              break;
            case "ERROR EMAIL DOESNT EXIST":
              this.alertError = true;
              this.msgerror = "Invalid Credentials!";
              this.$router.push("/login");
              break;
            case "ERROR PASSWORD INVALID":
              this.alertError = true;
              this.msgerror = "Invalid Credentials!";
              this.$router.push("/login");
              break;
            default:
              this.msgerror = "System Error! Try Later.";
              this.alertError = true;
              this.$router.push("/login");
          }
        })
        .catch(error => {
          // eslint-disable-next-line
          console.log(error);
        });
    }
  }
};
</script>
