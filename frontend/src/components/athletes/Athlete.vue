<template>
  <v-container grid-list-xs>
    <v-layout row>
      <v-flex xs12 md12>
        <v-toolbar color="grey lighten-2">
          <v-toolbar-title>Athlete Information</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12 md12>
        <v-card>
          <v-layout row justify-center>
            <v-flex xs12 md12>
              <v-card-title primary-title class="layout justify-center">
                <h3>{{this.athlete.name}}</h3>
              </v-card-title>
              <br>
              <br>
            </v-flex>
          </v-layout>
          <v-layout row justify-space-around>
            <v-flex xs12 md3>
              <div>
                <p align="center">
                  <b>Country:</b>
                  {{this.athlete.country}}
                </p>
              </div>
            </v-flex>
            <v-flex xs12 md3>
              <div>
                <p align="center">
                  <b>BirthDate:</b>
                  {{this.athlete.birth}}
                </p>
              </div>
            </v-flex>
            <v-flex xs12 md3>
              <div>
                <p align="center">
                  <b>Team:</b>
                  {{this.athlete.team.split("_")[1]}}
                </p>
              </div>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
    <Classification v-bind:athName="this.athlete.name"/>
  </v-container>
</template>

<script>
import axios from "axios";
import Classification from "./ListClassifications"
import { mapGetters } from "vuex";


export default {
  name: "athlete",
  computed: mapGetters(["getToken"]),
  components:{
    Classification
  },
  data() {
    return {
      athlete: {}
    };
  },
  mounted: function() {
    try {
      axios
        .get("http://localhost:2019/athlete/" + this.$route.params.id, {
          headers: { Authorization: "Bearer " + this.getToken }
        })
        .then(res => {
          this.athlete = res.data[0];
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>