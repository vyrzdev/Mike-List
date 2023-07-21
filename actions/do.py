import glob
import yaml
TOP = """
<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="main.css">
		<link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Courier+Prime&display=swap" rel="stylesheet">
	</head>
	<body>
		<div class="header">
			<div class="header-left">
				<h1 class="brand">
					Mike's List
				</h1>
				<p class="location">Hastings, UK</p>
			</div>
			<div class="header-right">
			</div>
		</div>
		<div class="main">
		<h1 class="events-section-title">What's on?</h1>
		<div class="events">
"""
BOTTOM = """
	</div>
		</div>
		<div class="ben-watermark">
			Built by <a href="https://github.com/vyrzdev">ben@vyrz.dev</a>
		</div>
	</body>
</html>
"""

event_files = glob.glob("../events/*.yaml")
build = str()
for filename in event_files:
    with open(filename, "r") as event_file:
        event_data = yaml.safe_load(event_file)
        try:
            html = f"""  
                <div class="event">
					<h1 class="event-title">
						<a class="event-title-link" href="{event_data['title']['artist_link']}">{event_data['title']['linked_part']}</a> {event_data['title']['unlinked_part']}
					</h1>
					<p class="event-blurb">
						{event_data['blurb_html']}
					</p>
					<p class="event-details">
						<span class="event-date">{event_data['date']}</span> -
						<a class="event-learn-more" href="{event_data['sales_link']}">Learn More and Buy Tickets</a>
					</p>
				</div>
            """
            build += "<br>" + html


        except KeyError as e:
            print("\033[0;31m"+f"Invalid event file, {filename}, missing key: {e.args[0]}"+"\033[0m")
            exit(1)

built = TOP + build + BOTTOM

with open("../index.html", "w+") as index_file:
    index_file.seek(0)
    index_file.write(built)
