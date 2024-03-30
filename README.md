# repo-notifier
sends a message to somewhere on telegram when a new app has been added to an altstore/esign/whatever repo

# usage
clone the repo, change the 4 constants at the top of the file, install [nim](https://nim-lang.org/install.html), `nim c -d:ssl -d:release --opt:speed repoNotifier.nim`

then you can use `./repoNotifier` to start :)
