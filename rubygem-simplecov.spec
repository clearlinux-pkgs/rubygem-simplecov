#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-simplecov
Version  : 0.10.0
Release  : 6
URL      : https://rubygems.org/downloads/simplecov-0.10.0.gem
Source0  : https://rubygems.org/downloads/simplecov-0.10.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-docile
BuildRequires : rubygem-rdoc

%description
SimpleCov [![Build Status](https://secure.travis-ci.org/colszowka/simplecov.png)][Continuous Integration] [![Dependency Status](https://gemnasium.com/colszowka/simplecov.png)][Dependencies] [![Code Climate](https://codeclimate.com/github/colszowka/simplecov.png)](https://codeclimate.com/github/colszowka/simplecov) [![Inline docs](http://inch-ci.org/github/colszowka/simplecov.png)](http://inch-ci.org/github/colszowka/simplecov)
=========
**Code coverage for Ruby**

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n simplecov-0.10.0
gem spec %{SOURCE0} -l --ruby > rubygem-simplecov.gemspec

%build
gem build rubygem-simplecov.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
simplecov-0.10.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/simplecov-0.10.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/cucumber.yml
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/doc/alternate-formatters.md
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/doc/commercial-services.md
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/doc/editor-integration.md
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_autoload.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_command_name.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_coverage_dir.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_deactivate_merging.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_formatters.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_merge_timeout.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_nocov_token.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_profiles.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_project_name.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/config_styles.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/cucumber_basic.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/maximum_coverage_drop.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/merging_test_unit_and_rspec.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/minimum_coverage.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/refuse_coverage_drop.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/rspec_basic.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/rspec_fails_on_initialization.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/rspec_groups_and_filters_basic.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/rspec_groups_and_filters_complex.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/rspec_groups_using_filter_class.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/rspec_without_simplecov.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/skipping_code_blocks_manually.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/step_definitions/html_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/step_definitions/simplecov_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/step_definitions/transformers.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/step_definitions/web_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/support/env.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/test_unit_basic.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/test_unit_groups_and_filters_basic.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/test_unit_groups_and_filters_complex.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/test_unit_groups_using_filter_class.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/test_unit_without_simplecov.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/features/unicode_compatiblity.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/command_guesser.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/defaults.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/exit_codes.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/file_list.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/formatter/multi_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/formatter/simple_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/jruby_fix.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/last_run.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/merge_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/no_defaults.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/profiles.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/railties/tasks.rake
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/result.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/result_merger.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/source_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/lib/simplecov/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/simplecov.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/cucumber.yml
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/features/step_definitions/my_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/features/support/env.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/features/test_stuff.feature
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/lib/faked_project.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/lib/faked_project/framework_specific.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/lib/faked_project/meta_magic.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/lib/faked_project/some_class.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/spec/faked_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/spec/forking_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/spec/meta_magic_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/spec/some_class_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/test/faked_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/test/meta_magic_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/test/some_class_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/faked_project/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/app/controllers/sample_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/app/models/user.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/deleted_source_sample.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/frameworks/rspec_bad.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/frameworks/rspec_good.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/frameworks/testunit_bad.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/frameworks/testunit_good.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/iso-8859.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/resultset1.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/resultset2.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/sample.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/fixtures/utf-8.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/shoulda_macros.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_1_8_fallbacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_command_guesser.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_deleted_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_file_list.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_filters.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_merge_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_result.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_return_codes.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_source_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-0.10.0/test/test_source_file_line.rb
/usr/lib64/ruby/gems/2.3.0/specifications/simplecov-0.10.0.gemspec
