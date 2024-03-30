import os, uri, sugar, jsony, strformat, httpclient

# change these!

const
    bot_token: string = ""
    chat_id: string = ""
    repo_link: string = ""
    repo_name: string = ""

#####

type
    AppsTable = object
        name: string

    RepoResp = object
        name: string
        apps: seq[AppsTable]

proc fetchRepo(): seq[string] =
    var client: HttpClient = newHttpClient()
    defer: client.close()

    let resp: RepoResp = client.getContent(repo_link).fromJson(RepoResp)
    result = newSeqOfCap[string](resp.apps.len)

    for app in resp.apps:
        result.add(app.name)

proc sendNoti(newApps: seq[string]): void =
    var client: HttpClient = newHttpClient()
    defer: client.close()

    for app in newApps:
        echo &"notifying about {app} !"
        discard client.postContent(
            fmt"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}" &
                "&text=" & encodeUrl(&"{app} has been added to the {repo_name}!"))
        sleep(5000)  # 5 seconds

var current: seq[string] = fetchRepo()

while true:
    sleep(120000)  # 2 minutes
    let newApps: seq[string] = collect(newSeq):
        for app in fetchRepo():
            if not current.contains(app): app

    sendNoti(newApps)
