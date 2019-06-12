<template>
  <v-container grid-list-xs>
    <ListTeams/>
  </v-container>
</template>

<script>
import ListTeams from "../components/teams/ListTeams";

export default {
  name: "teams",
  components: {
    ListTeams
  }
};
</script>
