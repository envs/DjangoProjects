var rpaApplications = {

	"schema": {
		"title":"asdasd",
		"type": "array",
        "items": {
            "type": "object",
            "properties": {
                "applicationType": {
                    "type": "number",
                    "title": "RPA Application Type",
                    "enum": [1, 3, 3, 5]
                },                                  
                "numberOfScreens": {
                    "title": "Number of Screens",
                   "type": "integer"                                            
                },
                "numberOfActionsPerScreen": {
                    "type": "integer",
                    "title": "Number of actions per screen"                                            
                },
                "complexity": {
                    "type": "number",
                    "title": "Complexity",
                    "enum": [1, 1.5, 2.5]
                },    
            }
        }
	},


	"options": {
		"type": "table",
        "label": "RPA Application",
        "items": {
            "fields": {                
                "applicationType": {
                    "default":1,
                    "removeDefaultNone": true,
                    "type": "select",
                    "optionLabels": ["Web", "Desktop", "Mainframe", "Citrix"]
                },
                "numberOfScreens": {
                    "default":3
                }, 
                "numberOfActionsPerScreen": {
                    "default":10
                    
                },
                "complexity": {
                    "default":1,
                    "removeDefaultNone": true,
                    "type": "select",
                    "optionLabels": ["Easy", "Mid-Complex", "Complex"]
                }
            }
        }
	}
}