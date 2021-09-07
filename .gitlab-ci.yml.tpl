stages:
  - run
#  - test
#  - push

pipeline_ok:
    stage: run
    script:
        - echo "Pipeline running!"
        
