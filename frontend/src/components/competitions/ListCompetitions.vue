<template>
  <v-layout row wrap>
    <v-flex xs12 md12>
      <v-toolbar color="grey lighten-2">
        <v-toolbar-title>Events</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-toolbar>
      <v-text-field v-model="search" append-icon="search" label="Search Competition" single-line hide-details></v-text-field>
      <v-data-table :headers="headers" :items="competitions" class="elevation-1" :search="search">
        <template v-slot:no-data>
          <v-alert :value="true" color="error" icon="red">Sorry, nothing to display here :(</v-alert>
        </template>

        <template slot="items" slot-scope="props">
          <tr @click="rowClicked(props.item)">
            <td class="text-xs-center">{{ props.item.date }}</td>
            <td class="text-xs-center">{{ props.item.names}}</td>
            <td class="text-xs-center">{{ props.item.country }}</td>
            <td class="text-xs-center">{{ props.item.class }}</td>
          </tr>
        </template>
      </v-data-table>
    </v-flex>
  </v-layout>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";


export default {
  name: "listCompetitions",
  computed: mapGetters(["getToken"]),
  methods: {
    rowClicked(item) {
      this.$router.push("/competitions/" + item.names);
    }
  },
  data() {
    return {
      competitions: [],
      search: '',
      headers: [
        { text: "Date", value: "date", align: "center" },
        { text: "Name", value: "names", align: "center", sortable: false },
        { text: "Country", value: "country", align: "center", sortable: false },
        { text: "Class", value: "class", align: "center" }
      ]
    };
  },
  mounted: function() {
    try {
      axios
        .get("http://localhost:2019/race/all",{
          headers: { Authorization: "Bearer " + this.getToken }
        })
        .then(res => {
          this.competitions = res.data;
        })
        // eslint-disable-next-line
        .catch(err => console.log(err));
    } catch (e) {
      return e;
    }
  }
};
</script>
