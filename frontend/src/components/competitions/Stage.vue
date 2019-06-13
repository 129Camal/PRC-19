<template>
  <v-container grid-list-xs>
    <v-layout row>
      <v-flex xs12 md12>
        <v-toolbar color="grey lighten-2">
          <v-toolbar-title >
            Classification of {{this.$route.params.stage}} -
            <b>{{this.$route.params.id}}</b>
          </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-data-table :headers="headers" :items="results" class="elevation-1">
          <template v-slot:no-data>
            <v-alert
              :value="true"
              color="error"
              icon="red"
            >Sorry, points classification not available! :(</v-alert>
          </template>

          <template slot="items" slot-scope="props">
            <tr>
              <td class="text-xs-center">{{ props.item.rank }}</td>
              <td class="text-xs-center">{{ props.item.name}}</td>
              <td class="text-xs-center">{{ props.item.team }}</td>
              <td class="text-xs-center">{{ props.item.value}}</td>
            </tr>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "points",
  data() {
    return {
      results: [],
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
        .get("http://localhost:2019/race/" + this.$route.params.id + "/stage/" + this.$route.params.stage)
        .then(res => {
          this.results = res.data;
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>