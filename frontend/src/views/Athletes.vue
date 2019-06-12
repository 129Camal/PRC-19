<template>
  <v-container grid-list-xs>
    <ListAthletes/>
  </v-container>
</template>

<script>
import ListAthletes from "../components/athletes/ListAthletes";

export default {
  name: "people",
  components: {
    ListAthletes
  }
};
</script>
