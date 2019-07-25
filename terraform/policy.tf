resource "aws_iam_policy" "s3_policy" {
  name   = "s3_policy"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
        "Effect": "Allow",
        "Action": "s3:*",
        "Resource": [
            "arn:aws:s3:::${var.s3_bucket}",
            "arn:aws:s3:::${var.s3_bucket}/*"
        ]
    }
  ]
}
EOF
}