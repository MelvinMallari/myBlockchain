import datetime as date

def create_genesis_block():
  # Manually construct the genesis block
  return Block(0, date.datetime.now(), "Bailing out the banks again", "0")
