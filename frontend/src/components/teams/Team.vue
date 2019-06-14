<template>
  <v-container>
    <v-layout row wrap justify-space-around>
      <v-flex xs12 md6>
        <h1 align="center">{{this.information.name}}</h1>
        <br>
        <v-img
          :src="'http://ucibws.uci.ch/api/WebResources/ModulesData/Teams/2019/ROA/Jerseys/WTT//ROA-WTT_' + this.$route.params.id + '_2019.jpg'"
          aspect-ratio="2"
          contain
        ></v-img>
      </v-flex>
      <v-flex xs12 md6>
        <br>
        <v-card>
          <v-card-title>
            <h4>
              <i>Team Information</i>
            </h4>
          </v-card-title>
          <v-list dense>
            <v-list-tile>
              <v-list-tile-content>Code:</v-list-tile-content>
              <v-list-tile-content class="align-end">{{ this.$route.params.id }}</v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>Country:</v-list-tile-content>
              <v-list-tile-content class="align-end">
                <div>
                  <country-flag :country="this.information.country" size="normal"/>
                </div>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>Continent:</v-list-tile-content>
              <v-list-tile-content class="align-end">{{ this.information.continent }}</v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>Category:</v-list-tile-content>
              <v-list-tile-content class="align-end">{{ this.information.category }}</v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>Email:</v-list-tile-content>
              <v-list-tile-content class="align-end">{{ this.information.email }}</v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>Website:</v-list-tile-content>
              <v-list-tile-content class="align-end">
                <a :href="this.information.website">{{ this.information.website }}</a>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
    <br>
    <br>
    <v-layout row justify-space-around>
      <ListTeamAthlete/>
      <ListTeamStaff/>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import CountryFlag from "vue-country-flag";
import ListTeamAthlete from "./ListTeamAthlete";
import ListTeamStaff from "./ListTeamStaff";
import { mapGetters } from "vuex";

export default {
  name: "team",
  computed: mapGetters(["getToken"]),
  components: {
    CountryFlag,
    ListTeamAthlete,
    ListTeamStaff
  },
  data() {
    return {
      information: {},
      headers: [
        { text: "Position", value: "rank", align: "center" },
        { text: "Name", value: "name", align: "center", sortable: false },
        { text: "Team", value: "team", align: "center", sortable: false },
        { text: "Result", value: "value", align: "center", sortable: false }
      ]
    };
  },
  mounted: function() {
    try {
      axios
        .get("http://localhost:2019/team/" + this.$route.params.id, {
          headers: { Authorization: "Bearer " + this.getToken }
        })
        .then(res => {
          this.information = res.data[0];
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>

