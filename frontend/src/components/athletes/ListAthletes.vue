<template>
  <v-layout row wrap>
    <v-flex xs12 md12>
      <h1 align="center">List of Professional Riders</h1>
      <v-data-table :headers="headers" :items="members" class="elevation-1">
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
      this.$router.push("/members/" + item.name);
    }
  },
  data() {
    return {
      members: [],
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
        .get("http://192.168.1.83:2019/athlete")
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