package main

import (
	"context"
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	pb "test_grpc_tavern/proto"
)

type server struct {
	pb.UnimplementedCalculatorServer
}

func (s *server) Add(ctx context.Context, req *pb.CalcRequest) (*pb.CalcResponse, error) {
	return &pb.CalcResponse{Result: req.A + req.B}, nil
}

func (s *server) Subtract(ctx context.Context, req *pb.CalcRequest) (*pb.CalcResponse, error) {
	return &pb.CalcResponse{Result: req.A - req.B}, nil
}

func (s *server) Multiply(ctx context.Context, req *pb.CalcRequest) (*pb.CalcResponse, error) {
	return &pb.CalcResponse{Result: req.A * req.B}, nil
}

func (s *server) Divide(ctx context.Context, req *pb.CalcRequest) (*pb.CalcResponse, error) {
	if req.B == 0 {
		return nil, status.Error(codes.InvalidArgument, "division by zero")
	}
	return &pb.CalcResponse{Result: req.A / req.B}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterCalculatorServer(s, &server{})
	log.Println("gRPC server listening on :50051")
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
