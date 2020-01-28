#!/usr/bin/python

import json

pl_json = """{
	"type": "modal",
	"title": {
		"type": "plain_text",
		"text": "Can Submit only once!",
		"emoji": true
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": true
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": true
	},
	"blocks": [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Welcome to Cornell Tech friend-match."
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "input",
			"label": {
				"type": "plain_text",
				"text": "What is your age group?"
			},
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select...",
					"emoji": true
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "20-23",
							"emoji": true
						},
						"value": "20-23"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "24-27",
							"emoji": true
						},
						"value": "24-27"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "28-30",
							"emoji": true
						},
						"value": "28-30"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "31+",
							"emoji": true
						},
						"value": "31+"
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
				"type": "plain_text",
				"text": "What is your favorite type of cuisine?"
			},
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select...",
					"emoji": true
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "American",
							"emoji": true
						},
						"value": "American"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Italian",
							"emoji": true
						},
						"value": "Italian"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Japanese",
							"emoji": true
						},
						"value": "Japanese"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Chinese",
							"emoji": true
						},
						"value": "Chinese"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thai",
							"emoji": true
						},
						"value": "Thai"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Mexican",
							"emoji": true
						},
						"value": "Mexican"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "French",
							"emoji": true
						},
						"value": "French"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Mediterranean",
							"emoji": true
						},
						"value": "Mediterranean"
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
				"type": "plain_text",
				"text": "What do you like to do outside of class? (multiple choices)"
			},
			"element": {
				"type": "multi_static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select...",
					"emoji": true
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Nothing but sleep",
							"emoji": true
						},
						"value": "Nothing but sleep"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Workout",
							"emoji": true
						},
						"value": "Workout"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "See friends",
							"emoji": true
						},
						"value": "See friends"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Drink",
							"emoji": true
						},
						"value": "Drink"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Explore NYC",
							"emoji": true
						},
						"value": "Explore NYC"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Study",
							"emoji": true
						},
						"value": "Study"
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
				"type": "plain_text",
				"text": "What are you doing for winter break? (multiple choices)"
			},
			"element": {
				"type": "multi_static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select...",
					"emoji": true
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "One of the Treks!",
							"emoji": true
						},
						"value": "One of the Treks!"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Traveling the world",
							"emoji": true
						},
						"value": "Traveling the world"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Going home to see family",
							"emoji": true
						},
						"value": "Going home to see family"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Staying in NYC and relaxing",
							"emoji": true
						},
						"value": "Staying in NYC and relaxing"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Winter sport activities",
							"emoji": true
						},
						"value": "Winter sport activities"
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
				"type": "plain_text",
				"text": "What is your favorite type of movie?"
			},
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select...",
					"emoji": true
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Comedy",
							"emoji": true
						},
						"value": "Comedy"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Romance",
							"emoji": true
						},
						"value": "Romance"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Horror",
							"emoji": true
						},
						"value": "Horror"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Indie",
							"emoji": true
						},
						"value": "Indie"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Foreign",
							"emoji": true
						},
						"value": "Foreign"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Drama",
							"emoji": true
						},
						"value": "Drama"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Suspense",
							"emoji": true
						},
						"value": "Suspense"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Action",
							"emoji": true
						},
						"value": "Action"
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
					"type": "plain_text",
					"text": "Have you enjoyed CT so far?"
				},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Yes"
						},
						"value": "Yes"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "No"
						},
						"value": "No"
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
					"type": "plain_text",
					"text": "How talkative would you say you are? (1 for “prefer to listen” and 5 for “can talk to a wall”)"
				},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "1"
						},
						"value": "1",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "2"
						},
						"value": "2",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "3"
						},
						"value": "3",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "4"
						},
						"value": "4",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "5"
						},
						"value": "5",
						"description": {
							"type": "plain_text",
							"text": "Can talk to a wall"
						}
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
					"type": "plain_text",
					"text": "Would you describe yourself extroverted or introverted?"
				},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Introverted"
						},
						"value": "Introverted",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "In between"
						},
						"value": "In between",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Extroverted"
						},
						"value": "Extroverted",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
					"type": "plain_text",
					"text": "Are you active in US politics?"
				},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Yes"
						},
						"value": "Yes",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "No"
						},
						"value": "No",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Not Really"
						},
						"value": "Not Really",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Prefer not to answer"
						},
						"value": "Prefer not to answer",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
					"type": "plain_text",
					"text": "What is your favorite type of vacation?"
				},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Relaxing on the beach"
						},
						"value": "Relaxing on the beach",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Exploring new countries and cultures"
						},
						"value": "Exploring new countries and cultures",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Visiting with friends and family"
						},
						"value": "Visiting with friends and family",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Active Adventure"
						},
						"value": "Active Adventure",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Sporty (hiking, skiing)"
						},
						"value": "Sporty (hiking, skiing)",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
					"type": "plain_text",
					"text": "When you try new things what do they tend to be?"
				},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Culture Related"
						},
						"value": "Culture Related",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Food Related"
						},
						"value": "Food Related",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Sports Related"
						},
						"value": "Sports Related",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Travel Related"
						},
						"value": "Travel Related",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
					"type": "plain_text",
					"text": "Cats or Dogs?"
				},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Cats"
						},
						"value": "Cats",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Dogs"
						},
						"value": "Dogs",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Neither"
						},
						"value": "Neither",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
					"type": "plain_text",
					"text": "Beer or Wine?"
				},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Wine"
						},
						"value": "Wine",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Beer"
						},
						"value": "Beer",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Prefer Not to drink"
						},
						"value": "Pref Not to drink",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					}
				]
			}
		},
		{
			"type": "input",
			"label": {
			  "type": "plain_text",
			  "text": "do you volunteer?"
			},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Always - whenever I have free time"
						},
						"value": "Always - whenever I have free time",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "I try but time is limited"
						},
						"value": "I try but time is limited",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "No - not really my thing"
						},
						"value": "No - not really my thing",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					}
				]
			}
		},
		{
			"type": "input",
            "optional": false,
			"label": {
				"type": "plain_text",
				"text": "Coffee or tea",
				"emoji": true
			},
			"element": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Coffee"
						},
						"value": "Coffee",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Tea"
						},
						"value": "Tea",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Neither"
						},
						"value": "Neither - I don't need caffine",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Both"
						},
						"value": "Both",
						"description": {
							"type": "plain_text",
							"text": " "
						}
					}
				]
			}
		}
	]
}"""

test_view = {
    "type": "modal",
    "submit": {
        "type": "plain_text",
        "text": "Submit",
        "emoji": True
    },
    "callback_id": "view_identifier",
    "title": {
        "type": "plain_text",
        "text": "Modal title"
    },
    "blocks": [
    {
        "type": "input",
        "label": {
            "type": "plain_text",
            "text": "Input label"
        },
        "element": {
            "type": "plain_text_input",
            "action_id": "value_indentifier"
        }
    }]
}

pl_view = (json.loads(pl_json))