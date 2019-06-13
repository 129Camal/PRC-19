<template>
  <v-layout row wrap v-if="members[0]">
    <v-flex xs12 md12>
      <v-toolbar color="grey lighten-2">
        <v-toolbar-title>List of Professional Riders</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>
      <v-text-field v-model="search" append-icon="search" label="Search Athlete" single-line hide-details></v-text-field>
      <v-data-table :headers="headers" :items="members" class="elevation-1" :search="search">
        <template v-slot:no-data>
          <v-alert :value="true" color="error" icon="red">Sorry, nothing to display here :(</v-alert>
        </template>

        <template slot="items" slot-scope="props">
          <tr @click="rowClicked(props.item)">
            <td class="text-xs-center">{{ props.item.name}}</td>
            <td class="text-xs-center">{{ props.item.teamname }}</td>
            <td class="text-xs-center">{{ props.item.c }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-flex>
  </v-layout>
</template>

<script>
import axios from "axios";


export default {
  name: "listAthletes",
  methods: {
    rowClicked(item) {
      this.$router.push("/athletes/" + item.athlete.split("_")[1]);
    }
  },
  data() {
    return {
      members: [],
      search: '',
      headers: [
        { text: "Name", value: "name", align: "center" },
        { text: "Team", value: "teamname", align: "center", sortable: false },
        { text: "Country", value: "country", align: "center", sortable: false }
      ]
    };
  },
  mounted: function() {
    try {
      axios
        .get("http://localhost:2019/athlete")
        .then(res => {
          this.members = res.data;
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>