gcloud config set project webhook-bot
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute scp --recurse ~/main.py webhook-bot:~/eif-bot
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud config set project webhook-bot
gcloud config set project webhookbot
gcloud config set project webhookbot-251409
gcloud compute scp --recurse ~/main.py webhook-bot:~/eif-bot
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud config set project testbot-232311
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/shedule_scrapper.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/shedule_scrapper.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/main.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/shedule_scrapper.py webhook-bot:~/eif-bot --zone us-central1-a
gcloud compute ssh webhook-bot --zone us-central1-a
gcloud compute scp --recurse ~/eif-bot/requirements.txt webhook-bot:~/eif-bot --zone us-central1-a
gcloud sql connect polls-instance --user=root --quiet
ls
git status
git init .
