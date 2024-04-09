class TestProject:

    def test_required_context(self, cookies):
        result = cookies.bake(extra_context={"project_slug": "my-project"})

        assert result.exception is None
        assert result.exit_code == 0

        assert result.project_path.name == "my-project"
        assert result.project_path.is_dir()

        circleci_path = result.project_path / ".circleci"
        assert circleci_path.is_dir()
        circleci_config_path = circleci_path / "config.yml"
        assert circleci_config_path.is_file()
