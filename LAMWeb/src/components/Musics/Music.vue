<template>
  <tr @click="updateMusic({ id: id, updates: { name : 'CLICADO!' } })">
    <td class="text-left">
      <div class="text-subtitle1"><strong>{{ music.name }}</strong></div>
      <small>{{ music.author }}</small>
    </td>
    <td class="text-right">
      <div>{{ music.type1 }}</div>
      <div>{{ music.type2 }}</div>
      <div>{{ music.type3 }}</div>
    </td>
  </tr>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    props : ['music','id'],
    methods : {
      ...mapActions('musics', ['updateMusic','deleteMusic']),
      promptToDelete (id) {
        this.$q.dialog({
          title: 'Confirm',
          message: 'Really delete?',
          ok: {
            push: true
          },
          cancel: {
            color: 'negative'
          },
          persistent: true
        }).onOk(() => {
          this.deleteMusic(id)
        })
      }
    }
  }
</script>

<style lang="scss">
</style>