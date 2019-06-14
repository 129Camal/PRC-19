<template>
  <v-container grid-list-xs>
    <v-layout row>
      <v-flex xs12 md12>
        <v-toolbar color="grey lighten-2">
          <v-toolbar-title>Registration</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <br>
        <br>

        <v-form>
          <v-text-field v-model="email" label="Email" required></v-text-field>

          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'visibility' : 'visibility_off'"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Password"
            required
            counter
            @click:append="show1 = !show1"
          ></v-text-field>
          <v-alert :value="alert" color="amber darken-1" icon="priority_high">
            <b>{{this.message}}</b>
          </v-alert>
          <v-btn @click="register">Registar</v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "register",

  data: () => ({
    show1: false,
    alert: false,
    message: "",
    email: "",
    password: ""
  }),

  methods: {
    register() {
      axios
        .post("http://localhost:2019/users/register", {
          email: this.email,
          password: this.password
        })
        .then(response => {
          switch (response.data.status) {
            case "OK":
              this.alert = false;
              this.$router.push("/login");
              break;
            case "ERROR EMAIL ALREADY IN USE":
              this.message = "Email Already in Use!";
              this.alert = true;
              this.$router.push("/register");
              break;
            case "ERROR PASSWORD SIZE 2 MIN":
              this.message = "Minimum Password Length 2!";
              this.alert = true;
              this.$router.push("/register");
              break;
            default:
              this.message = "System Error! Try Later.";
              this.alert = true;
              this.$router.push("/register");
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
