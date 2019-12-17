package config

import (
	"github.com/spf13/viper"
)

// IngressConfig represents the runtime configuration
type IngressConfig struct {
	Hostname             string
	KafkaBrokers         []string
	KafkaGroupID         string
	ConsumeTopic         string
	ProduceTopic         string
	OpenshiftBuildCommit string
}

// Get returns an initialized IngressConfig
func Get() *IngressConfig {

	options := viper.New()
	options.SetDefault("KafkaBrokers", []string{"kafka:29092"})
	options.SetDefault("KafkaGroupID", "ingress")
	options.SetDefault("ConsumeTopic", "{{cookiecutter.insights_platform_consume_topic}}")
	options.SetDefault("ProduceTopic", "{{cookiecutter.insights_platform_produce_topic}}")
	options.SetDefault("OpenshiftBuildCommit", "notrunninginopenshift")
	options.AutomaticEnv()
	kubenv := viper.New()
	kubenv.SetDefault("Hostname", "Hostname_Unavailable")
	kubenv.AutomaticEnv()

	return &IngressConfig{
		Hostname:             kubenv.GetString("Hostname"),
		KafkaBrokers:         options.GetStringSlice("KafkaBrokers"),
		KafkaGroupID:         options.GetString("KafkaGroupID"),
		ConsumeTopic:         options.GetString("ConsumeTopic"),
		ProduceTopic:         options.GetString("ProduceTopic"),
		OpenshiftBuildCommit: options.GetString("OpenshiftBuildCommit"),
	}
}
