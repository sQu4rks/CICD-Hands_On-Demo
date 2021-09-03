Feature: Create and retrieve a new entry

    Scenario: Add a new entry
        Given a request url http://127.0.0.1:8010/api/posts
            And a request json payload
                """
                {
                    "author": "integration_test",
                    "text": "Sample from integration test"
                }
                """
            When the request sends POST
            Then the response status is CREATED
    
    Scenario: Get all entries
        Given a request url http://127.0.0.1:8010/api/posts
        When the request sends GET
        Then the response status is OK
            And the response json matches
                """
                {
                    "title": "PostPage",
                    "type": "object",
                    "properties": {
                        "size": {"type": "number"},
                        "length": {"type": "number"},
                        "start": {"type": "number"},
                        "items": {"type": "array"}
                    },
                    "required": ["size", "length", "start", "items"]

                }
                """
            And the response json at $.start is equal to 0