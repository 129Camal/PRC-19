<template>
<v-layout row wrap>
  <v-flex xs12 md12>
  <h1 align="center">List of Professional Teams</h1>
  <v-data-table :headers="headers" :items="teams" class="elevation-1">
    <template v-slot:no-data>
      <v-alert :value="true" color="error" icon="red">Sorry, nothing to display here :(</v-alert>
    </template>

    <template slot="items" slot-scope="props">
      <tr @click="rowClicked(props.item)">
        <td class="text-xs-center">{{ props.item.team.split("_")[1]}}</td>
        <td class="text-xs-center">{{ props.item.name }}</td>
        <td class="text-xs-center">{{ props.item.continent}}</td>
      </tr>
    </template>
  </v-data-table>
  </v-flex>
</v-layout>
</template>

<script>
import axios from "axios";

export default {
  name: "listTeams",
  methods: {
    rowClicked(item) {
      this.$router.push("/teams/" + item.team.split("_")[1]);
    }
  },
  data() {
    return {
      teams: [],
      headers: [
        { text: "Code", value: "code", align: "center"},
        { text: "Name", value: "name", align: "center", sortable: false},
        { text: "Continent", value: "continent", align: "center", sortable: false }
      ]
    };
  },
  mounted: function() {
    try {
      axios.get("http://192.168.1.83:2019/team")
        .then(res => {
          this.teams = res.data;
          
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>