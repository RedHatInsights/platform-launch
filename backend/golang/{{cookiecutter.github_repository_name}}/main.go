package main

import (
	"context"
	"fmt"

	"github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}/config"
	l "github.com/{{cookiecutter.github_organization_name}}/{{cookiecutter.github_repository_name}}/logger"
	"github.com/segmentio/kafka-go"
)

func main() {
	cfg := config.Get()
	l.InitLogger()

	consumer := kafka.NewReader(kafka.ReaderConfig{
		Brokers: cfg.KafkaBrokers,
		GroupID: cfg.KafkaGroupID,
		Topic:   cfg.ConsumeTopic,
	})

	producer := kafka.NewWriter(Kafka.WriterConfig{
		Brokers:  cfg.KafkaBrokers,
		Topic:    cfg.ProduceTopic,
		Balancer: &kafka.LeastBytes{},
	})

	for {
		m, err := consumer.ReadMessage(context.Background())
		if err != nil {
			break
		}
		fmt.Printf("Message contents: %s", string(m.Value))
	}

}
