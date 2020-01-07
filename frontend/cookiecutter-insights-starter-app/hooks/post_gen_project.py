import yaml

githubURL = 'https://github.com/{{ cookiecutter.github_organization_name}}/{{ cookiecutter.github_repository_name }}'
githubDeploymentRepo = f"{githubURL}-build"
appURL = '{{ cookiecutter.insights_platform_app_bundle}}/{{ cookiecutter.insights_platform_app_pathname }}'

d = {
    '{{ cookiecutter.insights_platform_app_display_name }}': {
        'title': '{{ cookiecutter.insights_platform_app_name }}',
        'api': {
            'versions': [ '{{ cookiecutter.insights_platform_api_version }}' ],
            'isBeta': [ 'Yes' ]
        },
        'channel': '{{ cookiecutter.slack_channel }}',
        'description': '{{ cookiecutter.insights_platform_app_description }}',
        'git_repo': githubURL,
        'deployment-repo': githubDeploymentRepo,
        'frontend': {
            'title': '{{ cookiecutter.insights_platform_app_display_name }}',
            'paths': [ appURL ]
        }
    }
}

with open('cloudservicesconfig.yml', 'w') as outfile:
    outfile.write(yaml.dump(d, default_flow_style=False, allow_unicode=True, sort_keys=False))
