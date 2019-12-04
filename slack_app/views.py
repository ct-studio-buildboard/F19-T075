#!/usr/bin/python

import json

pl_json = """{
  "type": "modal",
  "title": {
    "type": "plain_text",
    "text": "My App",
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
        "text": "Welcome to the ParentLINK experiment./n Add your info so we can find good friend recomendations for you!"
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "input",
      "element": {
        "type": "plain_text_input"
      },
      "label": {
        "type": "plain_text",
        "text": "What's your age?",
        "emoji": true
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "What is your favorite type of cuisine?"
      },
      "accessory": {
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
            "value": "0"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Italian",
              "emoji": true
            },
            "value": "1"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Japanese",
              "emoji": true
            },
            "value": "2"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Chinese",
              "emoji": true
            },
            "value": "3"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Thai",
              "emoji": true
            },
            "value": "4"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Mexican",
              "emoji": true
            },
            "value": "5"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "French",
              "emoji": true
            },
            "value": "6"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Mediterranean",
              "emoji": true
            },
            "value": "7"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Variety of cuisines.",
              "emoji": true
            },
            "value": "8"
          }
        ]
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "What do you like to do outside of class?"
      },
      "accessory": {
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
            "value": "value-0"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Workout",
              "emoji": true
            },
            "value": "value-1"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "See friends",
              "emoji": true
            },
            "value": "value-2"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Drink",
              "emoji": true
            },
            "value": "value-3"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Explore NYC",
              "emoji": true
            },
            "value": "value-4"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "study",
              "emoji": true
            },
            "value": "value-5"
          }
        ]
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "What are you doing for winter break?"
      },
      "accessory": {
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
            "value": "value-0"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Traveling the world",
              "emoji": true
            },
            "value": "value-1"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Going home to see family",
              "emoji": true
            },
            "value": "value-2"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "staying in NYC and relaxing",
              "emoji": true
            },
            "value": "value-3"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "staying in NYC and relaxing",
              "emoji": true
            },
            "value": "value-3"
          }
        ]
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "What is your favorite type of movie?"
      },
      "accessory": {
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
            "value": "0"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Romance",
              "emoji": true
            },
            "value": "1"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Horror",
              "emoji": true
            },
            "value": "2"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Indie",
              "emoji": true
            },
            "value": "3"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Foreign",
              "emoji": true
            },
            "value": "4"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Drama",
              "emoji": true
            },
            "value": "5"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Suspense",
              "emoji": true
            },
            "value": "6"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Action",
              "emoji": true
            },
            "value": "7"
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "Have you enjoyed CT so far?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Yes"
          },
          "value": "1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Yes"
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
              "text": "No"
            },
            "value": "-1",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "How talkative would you say you are?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "1"
          },
          "value": "1",
          "description": {
            "type": "plain_text",
            "text": "Prefer to listen"
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "1"
            },
            "value": "1",
            "description": {
              "type": "plain_text",
              "text": "Prefer to listen"
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
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "Would you describe yourself extroverted or introverted?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Extroverted"
          },
          "value": "1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Extroverted"
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
              "text": "Introverted"
            },
            "value": "-1",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          },
          {
            "text": {
              "type": "plain_text",
              "text": "In Between"
            },
            "value": "0",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "Are you active in US politics?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Yes"
          },
          "value": "-1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Yes"
            },
            "value": "-1",
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
            "value": "2",
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
            "value": "1",
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
            "value": "0",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "What is your favorite type of vacation?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Relaxing on the beach"
          },
          "value": "1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Relaxing on the beach"
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
              "text": "Exploring new countries and cultures"
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
              "text": "Visiting with friends and family"
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
              "text": "Active Adventure"
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
              "text": "Sporty (hiking, skiing)"
            },
            "value": "5",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "When you try new things what do they tend to be?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Culture Related"
          },
          "value": "1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Culture Related"
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
              "text": "Food Related"
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
              "text": "Sports Related"
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
              "text": "Travel Related"
            },
            "value": "4",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "Cats or Dogs?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Cats"
          },
          "value": "-1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Cats"
            },
            "value": "-1",
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
            "value": "1",
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
            "value": "0",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "Beer or Wine?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Wine"
          },
          "value": "-1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Wine"
            },
            "value": "-1",
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
            "value": "1",
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
            "value": "0",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "Do you volunteer?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Always - whenever i have free time"
          },
          "value": "1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Always - whenever i have free time"
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
              "text": "I try but time is limited"
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
              "text": "No - not really my thing"
            },
            "value": "3",
            "description": {
              "type": "plain_text",
              "text": " "
            }
          }
        ]
      }
    },
    {
      "type": "section",
      "fields": [
        {
          "type": "mrkdwn",
          "text": "Coffee or Tea?"
        }
      ],
      "accessory": {
        "type": "radio_buttons",
        "initial_option": {
          "text": {
            "type": "plain_text",
            "text": "Coffee"
          },
          "value": "1",
          "description": {
            "type": "plain_text",
            "text": " "
          }
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Coffee"
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
              "text": "Tea"
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
              "text": "Neither"
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
              "text": "Both"
            },
            "value": "4",
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