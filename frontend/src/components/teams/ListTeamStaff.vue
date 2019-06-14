<template>
  <v-flex xs12 md5>
    <v-toolbar color="grey lighten-2">
      <v-toolbar-title>Staff</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-data-table :headers="headers" :items="members" class="elevation-1">
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="red">Sorry, nothing to display here :(</v-alert>
      </template>

      <template slot="items" slot-scope="props">
        <tr @click="rowClicked(props.item)">
          <td class="text-xs-center">{{ props.item.name}}</td>
          <td class="text-xs-center">{{props.item.job}}</td>
        </tr>
      </template>
    </v-data-table>
  </v-flex>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "listTeamStaff",
  computed: mapGetters(["getToken"]),
  methods: {
    rowClicked(item) {
      this.$router.push("/members/" + item.ath.split("_")[1]);
    }
  },
  data() {
    return {
      members: [],
      headers: [
        { text: "Name", value: "name", align: "center" },
        { text: "Job", value: "job", align: "center", sortable: false }
      ]
    };
  },
  mounted: function() {
    try {
      axios
        .get("http://localhost:2019/staff/" + this.$route.params.id, {
          headers: { Authorization: "Bearer " + this.getToken }
        })
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