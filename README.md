# shOUT

*Sometimes it feels good to shout into the void*

## Usage:

### Listener
`python3 listen.py`

### Sender
`python3 send.py`
(Then type messages to shout, each line will be sent as a separate message)

OR

`python3 send.py <file>`

This will send the contents of the file as a single message, terminating the connection after sending the message
(so files can be piped into other files on the listener side)